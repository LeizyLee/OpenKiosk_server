<%--
  Created by IntelliJ IDEA.
  User: User
  Date: 2019-06-26
  Time: 오후 1:56
  To change this template use File | Settings | File Templates.
--%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
        pageEncoding="UTF-8" %>
    <%
        // 0: 인증 가능 사용자 및 비밀번호 목록.
        String[] users = {"Infighter", "Prist", "Assassin"};
        String[] passwords = {"ak47", "M4", "Uzi"};

        // 1: form 으로부터 전달된 데이터를 변수에 저장
        String id = request.getParameter("id");
        String pw = request.getParameter("pw");

        // 2: 사용자 인증
        String redirectUrl = "form_02.jsp?error=login-failed..";

        for(int i = 0; i < users.length; i++){
            if(users[i].equals(id) && passwords[i].equals(pw))
                redirectUrl = "welcome.jsp?id="+id;
        }

        response.sendRedirect(redirectUrl);
    %>
