from selenium import webdriver
import time
import datetime
import requests
import csv
import tkinter as tk
from tkinter import ttk
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

driver.get("https://tradingsim.com/simulator")