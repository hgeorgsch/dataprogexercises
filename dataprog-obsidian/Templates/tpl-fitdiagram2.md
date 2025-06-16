<style>
.diagramslide {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  overflow: hidden;
}
.diagramslide h1, .diagramslide h2, .diagramslide h3, .diagramslide h4, .diagramslide h5, .diagramslide h6 {
  margin: 0.5em 0 0.2em 0;
  padding: 0 1.5em;
  max-height: 12vh;
  flex: 0 0 auto;
}
.diagramslide .internal-embed,
.diagramslide img,
.diagramslide svg {
  flex: 1 1 0;
  margin-left: auto;
  margin-right: auto;
  display: block;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  max-height: 75vh;   /* You can tweak this */
  max-width: 60vw;
  object-fit: contain;
}
.diagramslide .credit {
  margin: 0.2em 0 0.5em 0;
  padding: 0 1.5em;
  font-size: 0.4em !important;
  max-height: 10vh;
  flex: 0 0 auto;
  color: #888;
}

</style>

<div class="diagramslide">
  <% content %>
  <div class="credit">
  <% credit %>
  </div>
</div>

