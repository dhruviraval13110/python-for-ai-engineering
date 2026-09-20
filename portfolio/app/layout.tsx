import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Dhruvi Raval | AI/ML Engineer in Progress',
  description: 'Dhruvi Raval — Python, data, machine learning and AI engineering portfolio.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en"><body>{children}</body></html>;
}
