[Sprunge](http://sprunge.us) is a basic pastebin, which accepts it's input through web requests. Designed for Linux users, sprunge is an easy way to pastebin text without having to actually use a web browser. The oh-my-zsh plugin is based on [http://www.shellperson.net/sprunge-pastebin-script/](this shellscript), author unknown.

# Usage
You can use sprunge in the following ways:

* **Pipes:**  `echo "hello there...testing sprunge"|sprunge`
* **Files:**   `sprunge test.txt`
* **Strings:** `sprunge "hello"`

# Notes:
If a filename is misspelled or doesn't have the necessary path description, it will NOT generate an error, but will instead treat it as a text string and upload it.