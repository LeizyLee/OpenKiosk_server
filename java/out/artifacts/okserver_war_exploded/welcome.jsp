<%--
  Created by IntelliJ IDEA.
  User: User
  Date: 2019-06-26
  Time: 오후 2:02
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <h1><%= request.getParameter("id") %>님 <small>반갑습니다.</small></h1>
    <a href="form.jsp">로그아웃</a>
</body>
</html>
