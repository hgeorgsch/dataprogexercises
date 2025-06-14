
<style>
  .reveal .diagramslide {
    display: flex;
    flex-direction: column;
    height: 100vh;
    padding: 1em;
    box-sizing: border-box;
  }

  .reveal .diagramslide h2 {
    margin: 0 0 0 0;
    font-size: 2em;
    text-align: center;
    margin-bottom: 0.5em;
  }

  .reveal .diagramslide .img-container {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
  }

  .reveal .diagramslide img {
    max-height: 100%;
    width: auto;
    height: 100%;
    object-fit: contain;
  }

  .reveal .diagramslide .credit {
    font-size: 18pt;
    text-align: right;
    margin-top: 1em;
  }
</style>

<div class="diagramslide">
  <% heading %>
  <div class="img-container">
    <% content %>
  </div>
  <% credit %>
</div>
