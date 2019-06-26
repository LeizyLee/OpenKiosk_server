<%--
  Created by IntelliJ IDEA.
  User: User
  Date: 2019-06-25
  Time: 오후 1:45
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Request API</title>
</head>
<body>
    <h1>
        <li>접속자 IP주소: <%= request.getRemoteAddr()%></li>
        <li>서버 이름: <%= request.getServerName() %></li>
        <li>요청 방식: <%= request.getMethod() %></li>
        <li>프로토콜: <%= request.getProtocol() %></li>
        <li>요청 URL: <%= request.getRequestURL() %></li>
    </h1>
</body>
</html>
