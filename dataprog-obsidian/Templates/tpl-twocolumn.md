<style>
  .reveal .twocolumnslide .credit {
     font-size: 18pt ;
  }
  
  .reveal .twocolumnslide  h1 {
     font-size: 32pt ;
     text-transform: none;
  }
  .reveal .twocolumnslide section img {
     object-fit: contain   ;
     height: 600px ;
     border: none ;
     margin: 10px ;
  } 
</style>

<div class="twocolumnslide">
<% content %>

<split even>


::: block

<% leftimage %>
<% leftcredit %> <!-- element class="credit" -->

:::

::: block

<% rightimage %>
<% rightcredit %> <!-- element class="credit" -->

:::

</split>
</div>
