<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
      <head>
        <title>Wonders of the World</title>
      </head>
      <body>
       <h1>Wonders of the World</h1>

       The <xsl:value-of select="ancient_wonders/wonder/name"/>
       is located in <xsl:value-of select="ancient_wonders/wonder/location"/>.

      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
