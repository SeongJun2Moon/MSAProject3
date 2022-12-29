import '../styles/table.css'


export default function ListForm({list}) {
    return (
        <>
        <h1 style={{textAlign:"center"}}>UserList</h1>
        <table className='type2'>
          <th>ID</th>
          <th>이메일</th>
          <th>비밀번호</th>
          <th>이름</th>
          <th>휴대폰번호</th>
          <th>생일</th>
          <th>주소</th>
          <th>직업</th>
          <th>취미</th>
          {list &&
            list.map(
              ({
                id,
                user_email,
                password,
                user_name,
                phone,
                birth,
                address,
                job,
                user_interests,
              }) => (
                <tr key={id}>
                  <td>{id}</td>
                  <td>{user_email}</td>
                  <td>{password}</td>
                  <td>{user_name}</td>
                  <td>{phone}</td>
                  <td>{birth}</td>
                  <td>{address}</td>
                  <td>{job}</td>
                  <td>{user_interests}</td>
                </tr>
              )
            )}
        </table>
        </>
    )
}