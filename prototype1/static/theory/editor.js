
document.addEventListener("DOMContentLoaded",
function()
{ var Delta = Quill.import('delta');
 var quills = {}
 document.querySelectorAll('div').forEach((item)=>{
     quills[item.id]= new Quill(`${item.id}`,{
        modules: {
            toolbar: true
        },
        placeholder: 'Compose an epic...',
        theme: 'snow'
        });
 })
var quill = new Quill('#editor-container', {
modules: {
    toolbar: true
},
placeholder: 'Compose an epic...',
theme: 'snow'
});})

// // Store accumulated changes
// var change = new Delta();
// quill.on('text-change', function(delta) {
// change = change.compose(delta);
// });
// $("button").click(function(){
//     $.post("{% url 'addContent' %}", { 
//         doc: JSON.stringify(quill.getContents())
//     });
// })
// $("#submit_btn").click(function(){
//     $.ajaxSetup({
//     headers: { "X-CSRFToken": '{{csrf_token}}' }
// });
//             $.ajax({
//                 type:"post",
//                 url:"{% url 'addContent' %}",
//                 data:{
//                     doc: JSON.stringify(quill.getContents())
//                 },
//                 success:function(data,status,xhr){
//                     location.reload();
//                 },
//             });
//         });
// // Check for unsaved data
// window.onbeforeunload = function() {
// if (change.length() > 0) {
//     return 'There are unsaved changes. Are you sure you want to leave?';
// }
// }
