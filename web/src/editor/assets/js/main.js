javaEditor = CodeMirror.fromTextArea(document.getElementById("content"), {
    lineNumbers: true,
    styleActiveLine: true,
    matchBrackets: true,
    tabSize: 4,
    mode: "text/x-java"
});

$(document).ready(function() {
    javaEditor.setOption("theme", "oceanic");
});