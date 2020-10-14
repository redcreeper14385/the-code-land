# This simple snippet will demonstrate how easy is to change your default bash prompt on any linux machine using bash
# Output of the prompt will look something like this:
#
#┌─⭘ user in ~/Projects/the-code-land at 16:11:48 (master)
#└─⭘
#
# First is [user] in [working directory] at [current time] (if git repo, this is what branch you are in).
# And it has colors based on your terminal theme.
#
# You can modify any part to make it look what you want. This is what I use.

# there are variables with color coding, see https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html for more info
txtcyn='\[\e[0;96m\]'
txtred='\[\e[31m\]'
txtyel='\[\e[0;33m\]'
txtwhi='\[\e[37m\]'
txtblu='\[\e[34m\]'

# some more formatting, explained also in the link above
bold=$(tput bold)
normal=$(tput sgr0)

# this function checks if you are in git repository and if yes, returns branch name
function gitBranch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# this line defines how will the promt look like. At the start there is ┌─⭘ just to make it look interesting
# and on the new line is └─⭘ that optically connects the two lines
#
# the rest is just text that is generated from current session in terminal, getting current user with \u, current working directory with \w
# current time with \$(date +'%T') and finally call of the previously defined function and evaluate its return value with \$(gitBranch)
export PS1="\n${txtyel}┌─⭘ ${bold}\u ${normal}${txtwhi}in ${txtcyn}\w ${txtwhi}at ${txtblu}\$(date +'%T') ${txtred}\$(gitBranch)${txtwhi}\n${txtyel}└─⭘ ${txtwhi}"

# you can use this method of color coding with just about anything
#
# TO USE THIS MODIFICATION:
# 1. copy the contents of the script and append it to ~/.bashrc file
# 2. exit the current session in terminal or run source ~./bashrc to see the changes
# 3. enjoy!
