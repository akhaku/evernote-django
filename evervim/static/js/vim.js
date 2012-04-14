//Global variables
var mode = MODE.NORMAL;
var row = 0;
var col = 0;

$(document).ready(function() {
  //var textField = $("#vimText");
  //textField.text("hello world");
  $(document).keypress(function (event) {
      event.preventDefault();
      keyPress(String.fromCharCode(event.which))
  });
  $(document).keyup(function (event) {
      if(event.which == KEYCODE.ESCAPE)
        vim_escape();
  });
  //console.log(textToLineList(textField.text(), 3));
});

var KEYCODE = {
  ESCAPE: 33
};

var MODE = {
  NORMAL: 0,
  INSERT: 1
};


function keyPress(c)
{
  if(mode == MODE.INSERT) {
    console.log("In insert mode with key " + c);
  }
  else if(mode == MODE.NORMAL) {
    if(c == 'i') {
      mode = MODE.INSERT;
    }
  }
  console.log("Key " + c);
}

function vim_escape()
{
  mode = MODE.NORMAL;
}

function insertCharacter(c)
{
  //TODO: work here
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
