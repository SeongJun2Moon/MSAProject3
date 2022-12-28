import axios from 'axios'
import {server, strokepath} from 'context'
export const stroke = req => axios.get(`${server}${strokepath}`, req)
