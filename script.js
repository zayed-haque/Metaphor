document.getElementById('submitButton').addEventListener('click', function() {

    let inputData = document.getElementById('inputData').value;

    let apiUrl = ''; 
    let headers = {
        "Content-Type": "application/json",
        "x-api-key": "YOUR_API_KEY" 
    };
    

    fetch(apiUrl, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify({ data: inputData })
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById('apiResponse').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
        document.getElementById('apiResponse').textContent = 'Error fetching data. Please try again later.';
    });
});
