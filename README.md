# feedback-generator
Feedback Generator API for Python

# Steps
```
!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

from feedback_generator import generator

for num in range(10):
    print(generator("coffee"))
```
