<!-- Variant of tpl-twocolumn using CSS flexbox.
  -- This does not work as intended yet. -->

<div class="twocolumnflex">
<% content %>

<split even>

::: block

<% leftimage %>
<% leftcredit %> <!-- element class="credit" -->

:::
<!-- element class="flexcolumn" -->

::: block

<% rightimage %>
<% rightcredit %> <!-- element class="credit" -->

:::
<!-- element class="flexcolumn" -->

</split>
</div>
