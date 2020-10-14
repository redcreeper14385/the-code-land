# Prerequisities: bash, yay, sudo, Arch based distro, .yay_pkgs file in home directory
#
# This script can be used to notify you on bash start that there are some packages you care about ready to be updated
#
# You need yay installed to use this out of the box without modifications, which comes hand in hand with the need
# of being on Arch based distribution

# Sample output of this script:
# Relevant package updates (3): kwayland, networkmanager-qt, plasma-framework
#
# So htere is list of keywords in file .yay_pkgs, separated by newlines. Those are not package names,
# but really the key words, which means that if you have 'code' here, it will match every package
# you have installed with 'code' word in it's name. Sometimes might come in handy, but if you want
# perfect matching, keep the names of packages there


# This function calls yay and redirects stderr and stdout to the /dev/null to silence any output.
# Simply calling 'yay' command asks for confirmation to update, so 'echo n' is there to say No.
# After that 'yay -Qu' returns the updatable packages and the rest is just text formatting to keep the names only
# and matching the results with the ~/.yay_pkgs keywords
function getRelevantUpdates() {
  echo n | yay 1,2> /dev/null && yay -Qu | grep -o '^\S*' |  grep -f ~/.yay_pkgs
  #if you want to have the file with keywords elsewhere, change the last argument of last grep above
}

# Here we just store the results of parsing and available updates in 'res' variable
res=$(getRelevantUpdates)

# And there is the output. '-e' switch allows us to use color coding which is better explained in prompt-formatting.sh script
# in this repository in same directory. First parentheses get the 'res' variable and count the words and display number.
# The rest of the string is just coloured echo with formated results - replaces spaces between names of packages with commas
echo -e "\e[39mRelevant package updates ($(echo ${res} | wc -w)): \e[92;1m$(echo ${res//[[:space:]]/, })"

# res freed from the memory
unset res


# IMPORTANT: yay needs to be used by sudoer account - have NOPASSWD option to your account in /etc/sudoers
# I simply have 'myusername ALL = NOPASSWD : ALL' to run every command without need to write password
# Otherwise the 'yay' command will get stuck. (You can specify that only yay doesn't ask for password)

# HOW TO USE
# 1. copy the contents of the script and append it to ~/.bashrc file
# 2. create or copy .yay_pkgs file and enter keywords separated by newlines
# 3. exit the current session in terminal or run source ~./bashrc to see the changes
# 4. enjoy!
