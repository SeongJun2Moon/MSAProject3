const samsungRoute = `/samsung/samsung`
const server = "http://127.0.0.1:8000/"

const samsungService = {
    samsungWords
}

const handleResponse = (response) => { 
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
}

async function samsungWords(){
    const res = await fetch(`${server}${samsungRoute}`)
    .then(handleResponse)
    .then(data => JSON.stringify(data)) //JSON.stringify() : object를 JSON으로 변환 
    .catch((error) => {
        alert('error :::: '+error);
    });
    return Promise.resolve(res);
}
export default samsungService