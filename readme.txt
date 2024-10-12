Requirement: Install docker, make

Install steps:
cd to working folder:
0. run 'make help' for more information 
1. run: 'make build_container'
2. run: 'make run' 

-> inside container's terminal: 
3 run './init_db.sh' and follow initial set up instructions ('chmod +x init.sh' if not executable)
4 run 'python3 fetch.py'
5 run 'python3 load.py'
6 run 'python3 display.py'   -> display is running localhost:5000             
