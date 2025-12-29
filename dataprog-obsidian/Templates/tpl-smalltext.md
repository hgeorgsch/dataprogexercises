
<style>
/* These styles are quite unique to the smalltext template, and therefore
 * they are kept here. 
 * It also shares .smallertext with tpl-quote-header
 */
  .reveal .smalltext img {
     height: 300px ;
     border: none ;
     margin: 10px ;
  } 
  .reveal .smalltext h2 {
     font-size: 28pt ;
     text-transform: none;
  }
  .reveal .smalltext .credit {
     font-size: 16pt ;
  }
</style>

<div class="smalltext smallertext">
<% content %>
<% credit %> <!-- element class="credit" -->
</div>
