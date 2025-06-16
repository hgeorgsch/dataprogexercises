<style>
.tableslide {
  height: 100vh;
  width: 100vw;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.tableslide .header {
  flex: 0 0 auto;
  padding: 0.5em 1em 0.2em 1em;
}

.tableslide .tablescaler {
  flex: 1 1 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 0 1em;
}

.tableslide .tablescaler-inner {
  font-size: <% fontsize %>;
}

.tableslide .credit {
  flex: 0 0 auto;
  text-align: center;
  padding: 0.3em 1em;
  font-size: 0.5em;
  color: #666;
}
</style>

<div class="tableslide">
  <div class="header"><% header %></div>
  <div class="tablescaler">
    <div class="tablescaler-inner">
      <% content %>
    </div>
  </div>
  <div class="credit"><% credit %></div>
</div>

