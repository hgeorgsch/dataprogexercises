<style>
  .reveal .smalltext .credit {
     font-size: 18pt ;
  }
  .reveal .smalltext section img {
     object-fit: contain   ;
     height: 300px ;
     border: none ;
     margin: 10px ;
  } 
  .reveal .smalltext h1 {
     font-size: 28pt ;
     text-transform: none;
     padding-top: 20px ;
  }
  .reveal .smalltext table td, th {
     font-size: 14pt ;
     text-align: center ;
  }
  .reveal .smalltext code {
     font-size: 14pt ;
     width: 800px ;
     line-height: 1.1 ;
  }
</style>

<div class="smalltext">
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
