
var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
xmlhttp.open("POST", "/json-handler");
xmlhttp.setRequestHeader("Content-Type", "application/json");
xmlhttp.send(JSON.stringify([
    {
        "formName": "Form",
        "formFields": [
            "phone"
        ]
    },
    {
        "formName": "FFDF",
        "formFields": [
            "Message",
            "your email",
            "name"
        ]
    },
    {
        "formName": "dsddasd",
        "formFields": [
            "phone",
            "Message",
            "your email"
        ]
    },
    {
        "formName": "",
        "formFields": [
            "phone"
        ]
    },
    {
        "formName": "Form",
        "formFields": [
            "phone"
        ]
    }
]));
