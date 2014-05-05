upstream compare_django {
	server unix:///var/local/compareit/compare_django.sock;
}
 
server {
	listen 80;
	server_name	compareit.com compareit;
	
	location /media  {
        alias /home/naruto/workspace/compare/src/Compare/media;
    }

    location /static {
        alias /home/naruto/workspace/compare/src/Compare/static;
    }
	
	location / {
		proxy_pass_header 	Server;
		proxy_set_header 	Host $http_host;
		proxy_redirect 		off;
		proxy_set_header 	X-Real-IP $remote_addr;
		proxy_set_header 	X-Scheme $scheme;
        uwsgi_pass  		compare_django;
        include     		./uwsgi_params;
    }
}