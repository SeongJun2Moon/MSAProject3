import * as React from 'react';
import 'bootstrap/dist/css/bootstrap.css'
import Box from "@mui/material/Box";
import { useRouter } from 'next/router';
import BottomNavigation from "@mui/material/BottomNavigation";
import BottomNavigationAction from "@mui/material/BottomNavigationAction";

export default function Navigation(){
  const router = useRouter()
  
  return (
    <>
   <Box>
      <BottomNavigation showLabels>
        <BottomNavigationAction 
          onClick={() => router.push("/")} 
          label="홈" />
        <BottomNavigationAction
          onClick={() => router.push("/Counter")}
          label="카운터"
        />
        <BottomNavigationAction
          onClick={() => router.push("/users/join")}
          label="회원가입"
        />
        <BottomNavigationAction
          onClick={() => router.push("/users/login")}
          label="로그인"
        />
        <BottomNavigationAction
          onClick={() => router.push("/users/list")}
          label="사용자 등록"
        />
        <BottomNavigationAction
          onClick={() => router.push("/article/write")}
          label="글쓰기"
        />
      </BottomNavigation>
    </Box>
    </>
      
  );
}
