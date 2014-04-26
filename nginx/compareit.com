upstream compare_django {
	server unix:///var/local/compareit/compare_django.sock;
}

upstream compare_ws {
	server unix:///var/local/compareit/compare_ws.sock;
}
 
server {
	listen 80;
	
	location /media  {
        alias /home/naruto/workspace/compare/src/Compare/media;
    }

    location /static {
        alias /home/naruto/workspace/compare/src/Compare/static;
    }
    
    location /ws {
    	proxy_pass_header 	Server;
		proxy_set_header 	Host $http_host;
		proxy_redirect 		off;
		proxy_set_header 	X-Real-IP $remote_addr;
		proxy_set_header 	X-Scheme $scheme;
        uwsgi_pass  		compare_ws;
        include     		./uwsgi_params;
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