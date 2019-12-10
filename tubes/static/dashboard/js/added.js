(function($) {
    //make post request
    $("button#dss-btn").click(function (event) {
        event.preventDefault();
        console.log("masuk woi");
        var sentObj;
        sentObj = {
            'age': parseInt(document.getElementById('age').value),
            'job_int': parseInt(document.getElementById('job').value),
            'marital_int': parseInt(document.getElementById('marital').value),
            'education_int': parseInt(document.getElementById('education').value),
            'default_int': parseInt(document.getElementById('def').value),
            'balance': parseInt(document.getElementById('balance').value),
            'housing_int': parseInt(document.getElementById('house').value),
            'loan_int': parseInt(document.getElementById('loan').value),
            'contact_int': parseInt(document.getElementById('contact').value),
            'duration': parseInt(document.getElementById('duration').value),
            'campaign': parseInt(document.getElementById('campaign').value),
            'pdays': parseInt(document.getElementById('pdays').value),
            'previous': parseInt(document.getElementById('previous').value),
            'poutcome_int': parseInt(document.getElementById('poutcome').value)
        }
        fetch("/dss", {
            method: "POST",
            headers: {
                "Accept":"application/json",
                "Content-Type":"application/json",
            },
            body: JSON.stringify(sentObj)
        }).then(async (response) => {
            const content =  await response.json();
            console.log(content);
            if (content.results < 0.05){
                if (sentObj['balance'] > 100){
                    $('h3#dss-result').html("This Customer needs special approach for this customer can afford term deposit");
                } else {
                    $('h3#dss-result').html("This Customer needs no approach, he wont join");
                }
            } else {
                $('h3#dss-result').html("This Customer should need no special approach, he/she likely to join term deposit");
            }
        })
    })
})(jQuery); // End of use strict