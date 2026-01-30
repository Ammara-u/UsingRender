export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('q');

  try {
    const response = await fetch(
      `https://your-api-endpoint.com/api/search?q=${encodeURIComponent(query || '')}`,
      {
        headers: {
          'Content-Type': 'application/json',
          // Add any auth headers here
        },
      }
    );

    const data = await response.json();
    return Response.json(data);
  } catch (error) {
    return Response.json({ error: 'Failed to fetch' }, { status: 500 });
  }
}