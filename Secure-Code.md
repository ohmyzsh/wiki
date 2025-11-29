<!-- prettier-ignore-start -->
> _This wiki is automatically published from [ohmyzsh/wiki](https://github.com/ohmyzsh/wiki). To edit this page,_
> _go to [ohmyzsh/wiki](https://github.com/ohmyzsh/wiki), make your changes and submit a Pull Request._
<!-- prettier-ignore-end -->

# Secure Code

Oh My Zsh runs directly in people's environments, and there's currently no alternative.
This is why it is paramount that our code is vetted and reviewed according to security
best practices, specifically targeting Zsh.

## General Guidelines

Follow these practices when contributing code that runs in users' shells:

- Least privilege: design code to run with the minimal permissions required. Avoid elevate-right operations (sudo, setuid) unless absolutely necessary and documented.
- Input validation and escaping: treat all external input as untrusted. Validate, constrain, and escape inputs (prefer arrays and properly quoted arguments; avoid building commands by concatenation).
- Minimize use of eval/source/command substitution: avoid dynamic evaluation. If necessary, tightly validate inputs and limit the scope of what can be executed.
- Safe error handling: return clear, minimal errors for operators but never leak secrets or sensitive environment/state in messages or logs.
- Secrets and sensitive data: never hard-code credentials. Avoid writing secrets to logs, shell history, cache, or world-readable files; unset sensitive variables as soon as they are no longer needed (e.g., unset SECRET_VAR).
- Secure file handling: use secure temporary files (mktemp), set restrictive permissions (umask, chmod), and avoid creating files in insecure locations.
- Logging and telemetry: avoid logging and telemetry as much as possible. If necessary, only log what is necessary and redact or hash sensitive fields, and ensure log storage is access-controlled (e.g., not world-readable such as `/tmp`).
- Dependencies and supply chain: prefer minimal, well-audited dependencies; pin and justify any third-party tools that run with elevated privileges.
- Review, testing, and CI: require peer review for changes, include automated checks (shellcheck, unit/integration tests), and run security-focused CI scans before release.
- Documentation: document any security-relevant design decisions, required privileges, and mitigation steps so reviewers can assess risk.

## Insecure patterns to avoid

> [!NOTE]
> Here, we use `read something` as a command to symbolize untrusted input.
> In real world scenarios, untrusted input usually comes from some other place.

### eval with untrusted input

**Past vulnerabilities:**

- [Issue #10414](https://github.com/ohmyzsh/ohmyzsh/issues/10414): Unsafe use of `eval` with untrusted input

#### Use case 1: Dynamic command execution

**Insecure pattern:**

```sh
read filename  # User input: "file; echo pwned"
eval "stat $filename"  # Executes: stat file; echo pwned
```

This pattern is often seen in more complex code where the command is determined dynamically:

```sh
somefunction() {
  local arg="$1" filename="$2"
  local cmd="" 

  case "$arg" in
  -s) cmd="stat" ;;
  -l) cmd="ls" ;;
  esac

  eval "$cmd $filename"  # VULNERABLE
}

# Attack example
somefunction -s "file; rm -rf $HOME"
```

**Better pattern:**

```sh
somefunction() {
  local arg="$1" filename="$2"
  local cmd="" 

  case "$arg" in
  -s) cmd="stat" ;;
  -l) cmd="ls" ;;
  esac

  # SECURE: Zsh handles argument parsing safely
  $cmd "$filename"
}
```

The shell correctly parses each parameter as part of the same command. Even if `$filename` contains `;`, it will not be parsed as the beginning of a new command.

What's preventing injection are not the quotes around `$filename`, but the fact that we are passing each argument separately
in the command. This way, zsh knows exactly what each argument is supposed to be in the parsing phase, before any variable expansion happens.

### Use case 2: Variable assignment

**Insecure pattern:**

This almost never makes sense:

```sh
read var  # User input: "file; echo pwned"
eval "foo=$var"  # Executes: foo=file; echo pwned
```

But this one is more common:

```sh
read var  # User input: "echo pwned; myvariable"
eval "$var=helloworld"  # Executes: echo pwned; myvariable=helloworld
```

**Better pattern:**

Use `typeset` (or `declare`, or any of the other built-in variable assignment commands):

```sh
read var
typeset "$var=helloworld"  # SECURE: throws error instead of executing
```

This approach throws an error on malicious input rather than executing arbitrary commands:

```sh
➜  var="file; echo pwned"
➜  typeset "$var=helloworld"
➜  typeset -p myvariable
typeset myvariable=helloworld

➜  var="echo pwned; myvariable"
➜  typeset "$var=helloworld"
typeset: not valid in this context: echo pwned; myvariable
```

### print -P with untrusted input

**Past vulnerabilities:**

- [Issue #10414](https://github.com/ohmyzsh/ohmyzsh/issues/10414): Command injection via `print -P` with untrusted input

#### Use case: displaying formatted output with prompt sequences

**Insecure pattern:**

```sh
setopt promptsubst
dailyquote="$(get_daily_quote_from_the_internet)"
print -P "%F{yellow}%B${dailyquote}%b%f"  # VULNERABLE
```

If `dailyquote` contains `$()` or backticks (`` ` ``), zsh will execute those commands.

**Better pattern:**

```sh
# Disable prompt substitution for untrusted content
setopt localoptions nopromptsubst
dailyquote="$(get_daily_quote_from_the_internet)"
print -P "%F{yellow}%B${dailyquote}%b%f"  

# Use `print` without `-P` to avoid prompt substitution
setopt promptsubst
dailyquote="$(get_daily_quote_from_the_internet)"
print "${fg[yellow]}${dailyquote}${reset_color}"
```

### Unescaped % characters in prompt functions

**Past vulnerabilities:**

- [CVE-2021-45444](https://www.cve.org/CVERecord?id=CVE-2021-45444): Command execution via crafted branch names in prompts (partially fixed in zsh 5.8.1)
- [Issue #10414](https://github.com/ohmyzsh/ohmyzsh/issues/10414): Unquoted % characters in prompt functions

#### Use case: Functions that output untrusted content in prompts

**Insecure pattern:**

```sh
gitbranch() {
  command git symbolic-ref --short HEAD
}
PROMPT='myuser:$(gitbranch) %% '  # VULNERABLE
```

Git branch names may contain `%` characters. In zsh versions older than 5.8.1 with `setopt promptsubst` enabled, this is vulnerable to [CVE-2021-45444](https://www.cve.org/CVERecord?id=CVE-2021-45444). An attacker could craft a malicious branch name to execute arbitrary commands.

**Better pattern:**

```sh
gitbranch() {
  local branch="$(command git symbolic-ref --short HEAD)"
  echo -n "${branch//\%/%%}"  # Escape all % characters
}
PROMPT='myuser:$(gitbranch) %% '  # SECURE
```

Functions that output untrusted content for use in `$PROMPT` or `$RPROMPT` must:
1. Escape all `%` characters by replacing them with `%%`
2. Be documented and named to indicate they are prompt-safe
3. Be used only in prompt contexts where this escaping is appropriate
