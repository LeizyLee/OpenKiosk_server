<%--
  Created by IntelliJ IDEA.
  User: User
  Date: 2019-06-25
  Time: 오후 2:17
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPEhtml>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
<h1>전달받은 데이터</h1>
<ul>
    <li>이 름: <%= request.getParameter("name") %></li>
    <li>이메일: <%= request.getParameter("email") %></li>
    <li>비밀번호: <%= request.getParameter("password") %></li>
</ul>
</body>
</html>