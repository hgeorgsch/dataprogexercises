<style>
.reveal .tableslide {
  height: 100vh;
  width: 100vw;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.reveal .tableslide .header {
  flex: 0 0 auto;
  padding: 0.5em 1em 0.2em 1em;
}

.reveal .tableslide .tablescaler {
  flex: 1 1 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 0 1em;
}

.reveal .tableslide .credit {
  flex: 0 0 auto;
  text-align: center;
  padding: 0.3em 1em;
  font-size: 0.5em;
  color: #666;
}
</style>

<div class="tableslide">
  <% header %>
  <div class="tablescaler">
      <% content %>
  </div>
  <div class="credit"><% credit %></div>
</div>
