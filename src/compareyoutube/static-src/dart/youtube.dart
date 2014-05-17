import "dart:html";
import "dart:core";
import "dart:collection";

class WebSocketClient {
	final static serviceUrl = "ws://localhost:8888";
	
	String serviceEndpointUrl;
	WebSocket ws;
	
	Map callbacks = new HashMap();
	
	WebSocketClient(String endpoint) {
		this.serviceEndpointUrl = this.getUrl(endpoint);
		this.initWebSocket();
	}
	
	String getUrl(String endpoint) {
  		return serviceUrl + "/" + endpoint;
	}
	
	void initWebSocket() {
		this.ws = new WebSocket(this.serviceEndpointUrl);
		
		this.ws.onMessage.listen((MessageEvent e) {
    		this.callbacks.values.forEach((callback) {
    			callback(e.data);
    		});
  		});
	}
	
	void sendMessage(String action, var params) {
		Message message = new Message();
  		message.action = action;
  		message.params = params;
	}
	
	void addCallback(String action, var callback) {
		//Change to set of callbacks
		callbacks[action] = callback;
	}
}

class YoutubeWebSocketClient {

	var webSocketClient;

	YoutubeWebSocketClient() {
		this.webSocketClient = new WebSocketClient("youtube");
		
		var inputElement = query("#id_add-youtube-url");
		
		// On inputElement change send a 'get_youtube' message
		
  		var outputElement = query("#id_add-youtube-form");
  		
  		this.webSocketClient.addCallback("get_youtube", (data) {
  			print(data);
  		});
	}
}

void main() {
  var ytws = new YoutubeWebSocketClient();
}
