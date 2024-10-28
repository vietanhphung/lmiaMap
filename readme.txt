🎲 Project Caerus / End-to-end Interactive LMIA Distribution Map
Oct 2024 - PresentOct 2024 - Present
Caerus (Greek mythology) - God of opportunity, luck and favorable moments.

This project began in response to recent changes in immigration policies. My friend and I aim to assist those struggling with the ever-changing regulations and facing challenges in connecting with employers willing to sponsor through LMIA. The project will provide valuable insights into the geographic distribution of employers across Canada, along with other key information such as job sponsorship titles, wage types, and more. All of this will be presented in an interactive map.

● Collect data from canada.ca Rest API, handled, transformed, formatted and uploaded to MySQL remote
server, followed Agile methodologies, closely monitored by a mentor
● Used collected data, transform and update geographical coordinate data with google maps API to create
an interactive map of Canada featured the distribution trends of LMIA results
● Implemented filter features to improve data analyzation and simplified Bash Commands using Make
● Set up reverse Proxy as a security feature to hide IP address of backend server
● Skills and Technologies: Python, MySQL, SSH, Docker, Plotly, Pandas, Ubuntu, Linux Server, Nginx, Flask

Live Demo Link https://vcforests.com/map



********** Prerequisites **************

Make sure you have the following installed:
Docker
Make


********** Installation **************

0. cd to folder
0.1 run 'make help' for more information 
1. run 'make build_container'
2. run 'make init_container'
====> app will run at localhost:5000/map



