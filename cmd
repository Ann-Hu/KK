1. Hub
ava -jar selenium-server-standalone-3.4.0.jar -role hub

2. Nodes
[Windows]
java -jar selenium-server-standalone-3.4.0.jar -role node  -hub http://localhost:4444/grid/register
java -jar selenium-server-standalone-3.4.0.jar -role node  -hub http://localhost:4444/grid/register -port 7777

[Ubuntu]
cd /home/annhu/桌面
java -jar selenium-server-standalone-3.4.0.jar -role node  -hub http://192.168.0.18:4444/grid/register
java -jar selenium-server-standalone-3.4.0.jar -role node  -hub http://192.168.0.18:4444/grid/register -port 7777

3. Console
http://localhost:4444/grid/console

==========================
Install Java on Ubuntu:
==========================
java -version
sudo apt-get install default-jre
