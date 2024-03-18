#!/bin/bash
echo "Would you like to install the newest version of python3.11-venv?[y/n]"
read -p "[>] " answer
if [ "$answer" = "y" ];then
    echo "Installing python3.11-venv now!"
    sudo apt install python3.11-venv
    python3 -m venv venv
    source venv/bin/activate
elif [ "$answer" = "n" ];then
    echo "Ok, not installing it!"
else
    echo "Invalid Input! Starting normally without python3.11-venv"
fi
python3 main.py