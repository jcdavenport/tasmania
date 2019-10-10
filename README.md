# Tasmania
CTO Challenge #8  
AI/Machine Learning with Python3 and the Ludwig toolbox for data classification.  

_for more info on the Ludwig toolbox, visit: https://github.com/uber/ludwig_  

---  

Pre-reqs:  
* Only tested on Linux OS  
* Run <code>sudo apt install libgmp3-dev</code> for Debian based systems. OR...  
* Run <code>sudo yum install gmp gmp-devel</code> for RedHat based systems.  
  
Use:  
* Clone this repo. 
* In the "data/" directory, place training and testing csv data into their proper folders.
* Create a virtualenv, and install the requirements with <code>pip install -r requirements.txt</code>
* Ensure pre-reqs have been installed for your Linux system.  
* Execute with <code>python app.py</code>  
* Final results will be stored in a folder labeled "results_0" which will automatically be created in the top-level
 directory.