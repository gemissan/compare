import "dart:html";
import "dart:core";

String serviceUrl = "localhost:8888";

String getUrl(String endpoint) {
  return serviceUrl + "/" + endpoint;
}

void sendMessage(String url, String action, var params, callback) {

  Message message = new Message();
  message.action = action;
  message.params = params;
}

dynamic setCheckedYoutubeObject(var outputContainer) {
  
  void f(Message message) {
  }
  
  return f;
}

dynamic checkYoutubeObject(var inputElement, var outputContaier) {
  
  void f() {
    sendMessage(
  	  getUrl("youtube"),
  	  "check",
  	  inputElement.value,
  	  setCheckedYoutubeObject(outputContaier));
 }
 
 return f;
}

void main() {
  var inputElement = query("#id_add-youtube-url");
  var outputElement = query("#id_add-youtube-form");
  
  var addYoutubeHandle = checkYoutubeObject(inputElement, outputElement);
  
  inputElement
    ..onChange.listen(addYoutubeHandle)
    ..onPaste.listen(addYoutubeHandle);
}
