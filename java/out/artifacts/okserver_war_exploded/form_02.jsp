<%--
  Created by IntelliJ IDEA.
  User: User
  Date: 2019-06-26
  Time: 오후 1:54
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
    <% if (request.getParameter("error") == null){ %>
        <h1>Please Login..</h1>
    <%} else {%>
        <h1><%= request.getParameter("error")%></h1>
    <% } %>

    <form action="authentication.jsp" method="post">
        <label>ID : </label>
        <input name="id" type="text"><br>

        <label>PW: </label>
        <input name="pw" type="password"><br>

        <input type="submit" value="로그인">
    </form>
</body>
</html>
