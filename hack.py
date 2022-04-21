class Hack:
    
    def __init__(self,host,ip,port,password):
        self.check_ip(ip)
        self.check_host(host)
        self.check_port(port)
        self.check_password(password)
        self.__host = host
        self.__ip = ip
        self.__port = port
        self.__password = password

    @classmethod
    def check_host(cls,host):
        hosts = host.split(".")
        d = all([True if i.isdigit()  else False for i in hosts])
        
        if len(hosts)!=4:
            raise TypeError('Incorrect Format')
        if d is False:
            raise TypeError('ip must be digit')
        r = all([True if int(i) in range(0,256) else False for i in hosts])
        if r is False:
            raise TypeError('Should be in range(0,255)')


    @classmethod
    def check_ip(cls,ip):
        ips = ip.split(".")
        d = all([True if i.isdigit()  else False for i in ips])
        
        if len(ips)!=4:
            raise TypeError('Incorrect Format')
        if d is False:
            raise TypeError('ip must be digit')
        r = all([True if int(i) in range(0,256) else False for i in ips])
        if r is False:
            raise TypeError('Should be in range(0,255)')

    @classmethod
    def check_port(cls,port):
        if not port.isdigit():
            raise('port should be int')
        elif int(port) not in range(1024,10000):
            raise TypeError('port shoul be in 1024-9999')

    @classmethod
    def check_password(cls,password):
        if not password.isdigit():
            raise TypeError('password only digits')


    @property
    def ip(self):
        return self.__ip
    @ip.setter
    def ip(self, ip):
        self.check_ip(ip)
        self.__ip = ip

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        self.check_host(host)
        self.__host = host

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.check_port(port)
        self.__port = port
        
    @property
    def password(self):
        return self.__password

    @password.setter
    def ps(self, password):
        self.check_password(password)
        self.__password = password

def filter_data(file_name):
    with open(file_name,'r') as f:
        data = f.readlines()

    host = data[0]
    host = host[host.find('=')+2:-1]

    ip = data[1]
    ip = ip[ip.find('=')+2:-1]

    port = data[2]
    port = port[port.find('=')+2:-1]

    password = data[3]
    password = password[password.find('=')+2:-1]
    return host,ip, port,password

host,ip,port,password = filter_data('data.txt')

hacker = Hack(host,ip,port,password)

print(hacker.__dict__)
hacker.port = '9999'
print(hacker.port)

print(hacker.__dict__)