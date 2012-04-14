$(document).ready(function() {
  var textField = $("#vimText");
  textField.text("hello world");
  $(document).keypress(function (event) {
      event.preventDefault();
      keyPress(String.fromCharCode(event.which))
  });
  console.log(textToLineList(textField.text(), 3));
});

function keyPress(c)
{
  console.log("Key " + c);
}

function textToLineList(text, lineLength)
{
  var textLength = text.length;
  var lines = [];
  var numLines = 0;
  var lineBegin = 0;
  for(var i = 0; i < textLength; i++) {
    if (text[i] == '\n') {
      lines[numLines] = text.substring(lineBegin, i);
      lineBegin = i + 1;
      numLines++;
    }
    else if(i - lineBegin + 1 >= lineLength) {
      lines[numLines] = text.substring(lineBegin, i + 1);
      lineBegin += lineLength;
      numLines++;
    }
  }
  if (lineBegin < textLength) {
    lines[numLines] = text.substring(lineBegin);
  }
  return lines;
}
