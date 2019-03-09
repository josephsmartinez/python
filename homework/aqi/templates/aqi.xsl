<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
      <head>
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"/>
        <!-- Other CSS -->
        <style>
          body {
            display: -ms-flexbox;
            display: flex;
            -ms-flex-align: center;
            align-items: center;
            padding-top: 40px;
            padding-bottom: 40px;
            background-color: #f5f5f5;
          }
          figcaption{
            text-align: center;
          }
          h1{
           text-align: center;
          }

        </style>
        <title>Air Quality in <xsl:value-of select="all/data/city"/> </title>
      </head>
      <body>
       <div class="container-fluid">
        <h1>Air Quality in <xsl:value-of select="all/data/city"/></h1>
          <table class="table">
            <thead>
              <tr>
                <th scope="col">City</th>
                <th scope="col">State</th>
                <th scope="col">country</th>
                <th scope="col">Latitude</th>
                <th scope="col">Longitude</th>
                <th scope="col">Timestamp</th>
                <th scope="col">Temperature</th>
                <th scope="col">Humidity</th>
                <th scope="col">Atmospheric Pressure</th>
                <th scope="col">Wind Direction</th>
                <th scope="col">Wind Speed</th>
                <th scope="col">AQI vaule in US Standards</th>
                <th scope="col">Main pollutant of US AQI</th>
              </tr>
            </thead>
            <tbody>
            <tr>
              <td><xsl:value-of select="all/data/city"/></td>
              <td><xsl:value-of select="all/data/state"/></td>
              <td><xsl:value-of select="all/data/country"/></td>
              <td><xsl:value-of select="all/data/location/coordinates[1]"/></td>
              <td><xsl:value-of select="all/data/location/coordinates[2]"/></td>
              <td><xsl:value-of select="all/data/current/weather/ts"/></td>
              <td><xsl:value-of select="all/data/current/weather/tp"/></td>
              <td><xsl:value-of select="all/data/current/weather/hu"/></td>
              <td><xsl:value-of select="all/data/current/weather/pr"/></td>
              <td><xsl:value-of select="all/data/current/weather/wd"/></td>
              <td><xsl:value-of select="all/data/current/weather/ws"/></td>
              <td><xsl:value-of select="all/data/current/pollution/aqius"/></td>
              <td><xsl:value-of select="all/data/current/pollution/mainus"/></td>
            </tr>
            </tbody>
          </table>
          <xsl:if test="all/data/current/weather/ic = '01d'">
          <img class="rounded mx-auto d-block" src="weather_icons/01d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Clear Sky (Day)</figcaption>
          </xsl:if>
          <xsl:if test="all/data/current/weather/ic = '01n'">
          <img class="rounded mx-auto d-block" src="weather_icons/01n.png" alt="Clear Sky (Day)"></img>
          <figcaption>Clear Sky (Night)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '02d'">
          <img class="rounded mx-auto d-block" src="weather_icons/02d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Overcast (Day)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '02n'">
          <img class="rounded mx-auto d-block" src="weather_icons/02n.png" alt="Clear Sky (Day)"></img>
          <figcaption>Overcast (Night)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '03d'">
          <img class="rounded mx-auto d-block" src="weather_icons/03d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Cloudy (Day)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '04d'">
          <img class="rounded mx-auto d-block" src="weather_icons/04d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Very Cloudy (Day)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '09d'">
          <img class="rounded mx-auto d-block" src="weather_icons/09d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Rain (Day)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '10d'">
          <img class="rounded mx-auto d-block" src="weather_icons/10d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Rain with Sun (Day)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '10n'">
          <img class="rounded mx-auto d-block" src="weather_icons/10n.png" alt="Clear Sky (Day)"></img>
          <figcaption>Rain (Night)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '11d'">
          <img class="rounded mx-auto d-block" src="weather_icons/11d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Thunder (Day)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '13d'">
          <img class="rounded mx-auto d-block" src="weather_icons/01d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Snow (Day)</figcaption>
          </xsl:if>
           <xsl:if test="all/data/current/weather/ic = '50d'">
          <img class="rounded mx-auto d-block" src="weather_icons/50d.png" alt="Clear Sky (Day)"></img>
          <figcaption>Wind (Day)</figcaption>
          </xsl:if>
          <img class="rounded mx-auto d-block" src="city.png" alt=""></img>
        </div>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
