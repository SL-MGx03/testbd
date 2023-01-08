echo "Cloning Repo...."
git clone https://github.com/Test-Area-59/brodcast /brodcast
cd /brodcast
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
