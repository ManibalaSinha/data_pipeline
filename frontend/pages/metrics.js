export async function getServerSideProps() {
  const res = await fetch("http://localhost:8000/api/metrics"); // create a simple metrics endpoint in backend
  const metrics = await res.json();
  return { props: { metrics } };
}

export default function Metrics({ metrics }) {
  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Pipeline Metrics</h1>
      <ul>
        {metrics.map((m) => (
          <li key={m.id}>
            <strong>{m.name}</strong> – Success: {m.success_count}, Fail: {m.fail_count}
          </li>
        ))}
      </ul>
    </div>
  );
}
