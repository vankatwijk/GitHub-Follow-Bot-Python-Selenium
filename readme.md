# Project Title

Github bot to follow developers how are likely to follow you back

# Project Description

Github bot build with python and selenium to follow developers how are likely to follow you back.

# Requirments
install selenium
```
pip3 install selenium / pip install selenium (python 2)
```


Install ChromeDriver,
download the drivers from https://chromedriver.chromium.org/downloads make sure to download the version for the version of chrome you have installed, if its a different version your app won't work

```
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

other commands used
```
pip3 install virtualenv
source venv/bin/activate
```
# pre-requirements
```
nano secrets.py
then type "pw = XXXXX"
where XXXXX is your real password
```

# running the code
```
python -i main.py
exit()
```

## Built With

* [Python](hhttps://www.python.org/) - python language
* [selenium](hhttps://www.selenium.dev/) - Selenium automates browsers

## Authors

* **Hendrikus van Katwijk** - [Github](https://github.com/vankatwijk) - [Personal website](https://hpvk.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
