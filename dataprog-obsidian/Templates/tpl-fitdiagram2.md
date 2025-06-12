
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

.diagramslide .heading {
  flex: 0 0 auto;
  margin: 0.5em 0 0.25em 0;
  padding: 0 1em;
}

.diagramslide .internal-embed {
  display: flex;
  flex: 1 1 auto;
  align-items: center;
  justify-content: center;
  min-height: 0; /* critical for flex children */
}

.diagramslide .internal-embed img,
.diagramslide img {
  max-height: 50vh;
  max-width: 98vw;
  width: auto;
  height: auto;
  object-fit: contain;
  display: block;
}

/* For standalone <img> tags, just in case */
.diagramslide img {
  margin: 0 auto;
}

.diagramslide .credit {
  flex: 0 0 auto;
  font-size: 0.9em;
  color: #999;
  margin: 0.25em 1em 0.75em 1em;
  text-align: right;
}
</style>

<div class="diagramslide">
  <% heading %>
  <% content %>
  <% credit %>
</div>
