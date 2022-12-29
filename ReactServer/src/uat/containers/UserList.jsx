import '../styles/table.css'
import {server, users} from 'context'
import {useEffect, useState} from 'react'
import ListForm from 'uat/components/ListFrom'
import axios from 'axios'

export default function UserList() {
    const [list, setList] = useState([])
    useEffect(()=>{
        fetchList()
    }, [])
    const fetchList = () => {
        axios.get(`${server}${users}`)
        .then(res => {
            setList(res.data)
        })
        .catch(err => {
            alert(err)
        })
    }
    return (
        <>
            <ListForm list={list}/>
        </>
    )
}