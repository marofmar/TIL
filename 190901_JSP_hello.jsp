<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Hello JSP</title>
</head>
<body>
<h2>Mads' first JSP web page</h2>

<%
	int a = 10, b = 20;
out.print(a+b);
out.print("<br>");
%>

</body>
</html>
