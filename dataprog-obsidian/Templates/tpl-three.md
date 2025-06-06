<style>
  .reveal .twocolumnslide .credit {
     font-size: 18pt ;
  }
  .reveal .twocolumnslide {
     font-size: 21pt ;
  } 
  .reveal .twocolumnslide section img {
     object-fit: contain   ;
     height: 600px ;
     border: none ;
     margin: 10px ;
     font-size: 28pt ;
  } 
</style>

<div class="twocolumnslide">
<% content %>

<split even>


::: block
<% image1 %>
<% credit1 %> <!-- element class="credit" -->
:::

::: block
<% image2 %>
<% credit2 %> <!-- element class="credit" -->
:::

::: block
<% image3 %>
<% credit3 %> <!-- element class="credit" -->
:::


</split>
</div>
