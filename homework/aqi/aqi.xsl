<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html><head><title>Air Quality in Miami</title></head>
  <body>
    #Your code for displaying the table goes here



    ...
    #To display the weather icon, you can use an if statement in XSL as follows:

    <xsl:if test="all/data/current/weather/ic = ’01d’">
     <img src="weather_icons/01d.png" alt="Clear Sky (Day)"></img>
     <figcaption>Clear Sky (Day)</figcaption>
    </xsl:if>
    #Your code for displaying the weather icon continues here
    ...
  </body>
</html>
</xsl:template>
</xsl:stylesheet>