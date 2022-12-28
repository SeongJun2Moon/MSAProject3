import { stroke } from '../api'


const Stroke = () => {
    
    const onClick = () => {
        stroke().then(()=>{
            alert("됐어유")
        })
        .catch(()=>{
            alert("안됐어유")
        })
    }
    
    return (
        <>
            <button onClick={()=>onClick()}>뇌졸중</button>
        </>
    )
    
    
}


export default Stroke