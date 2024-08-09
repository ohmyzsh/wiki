#!/usr/bin/env zsh

pushd -- "$ZSH" || exit

setopt extended_glob
local plugin readme description
for plugin in plugins/*(:t); do
  readme="plugins/$plugin/README.md"

  # sed command explanation:
  # -n: suppress automatic printing of lines
  #
  # a. `N``: join the next line of input with the pattern space, including \n in the pattern
  # b. `s/\n/ /`: replace the newline character with a space (this joins the lines together)
  # c. `3,/^ /{ /^ /!p }`:
  #     - match from line 3 until the first line that starts with a space (i.e. the first empty line, because of (a) and (b))
  #     - print all lines except the delimiter line that starts with a space (again, the first empty line)
  #
  # Summary: get the first paragraph of the README file, which starts at line 3, and join all contiguous lines together
  description="$(awk '
    function lowercase_first_if_not_acronym(paragraph) {
      # Capture the first word, including markdown formatting
      if (match(paragraph, /^[^[:space:]]+/)) {
        first_word = substr(paragraph, RSTART, RLENGTH)

        # Extract only the alphabetical characters (remove any markdown formatting)
        gsub(/[^[:alpha:]]/, "", first_word)

        # If first_word contains only uppercase letters, return the paragraph as is
        if (first_word ~ /^[A-Z]+$/) {
          return paragraph
        }

        # Otherwise, lowercase the first letter of the first word
        first_letter = substr(paragraph, 1, 1)
        paragraph = tolower(first_letter) substr(paragraph, 2)
      }

      return paragraph
    }

    NR >= 3 {
      if (/^$/) { exit }
      paragraph = paragraph (paragraph ? " " : "") $0;
    }
    END {
      if (!length(paragraph)) { exit }
      print lowercase_first_if_not_acronym(paragraph);
    }' "$readme")"

  # Print the plugin name and description
  cat <<EOF
- [${plugin}](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/${plugin}): ${description}
EOF
done
