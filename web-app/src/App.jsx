import React, { useState, useEffect } from 'react';
import { manifest, allNotes, mcqBank, mainsBank } from './data/notesDatabase';
import TopNav from './components/TopNav';
import Sidebar from './components/Sidebar';
import TopicView from './components/TopicView';
import McqPracticeView from './components/McqPracticeView';
import MainsBankView from './components/MainsBankView';
import DashboardView from './components/DashboardView';
import ImageModal from './components/ImageModal';

export default function App() {
  const [activeTopicId, setActiveTopicId] = useState(() => {
    return allNotes[0]?.topic_id || 'APPSC-G1-HIST-01';
  });

  const [viewMode, setViewMode] = useState('notes'); // 'notes' | 'mcqs' | 'mains' | 'dashboard'
  
  const [sidebarOpen, setSidebarOpen] = useState(() => {
    try {
      const saved = localStorage.getItem('appsc_sidebar_open');
      if (saved !== null) return JSON.parse(saved);
    } catch {}
    return typeof window !== 'undefined' ? window.innerWidth >= 1024 : true;
  });

  const [searchQuery, setSearchQuery] = useState('');
  const [paperFilter, setPaperFilter] = useState('ALL');
  const [fontSizeMultiplier, setFontSizeMultiplier] = useState(1);
  const [modalImage, setModalImage] = useState(null);

  const [completedTopics, setCompletedTopics] = useState(() => {
    try {
      const saved = localStorage.getItem('appsc_completed_topics');
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  const [bookmarks, setBookmarks] = useState(() => {
    try {
      const saved = localStorage.getItem('appsc_bookmarks');
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('appsc_sidebar_open', JSON.stringify(sidebarOpen));
    } catch (e) {}
  }, [sidebarOpen]);

  useEffect(() => {
    try {
      localStorage.setItem('appsc_completed_topics', JSON.stringify(completedTopics));
    } catch (e) {}
  }, [completedTopics]);

  useEffect(() => {
    try {
      localStorage.setItem('appsc_bookmarks', JSON.stringify(bookmarks));
    } catch (e) {}
  }, [bookmarks]);

  const handleToggleComplete = (id) => {
    setCompletedTopics(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const handleToggleBookmark = (id) => {
    setBookmarks(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const handleSelectTopic = (id) => {
    setActiveTopicId(id);
    setViewMode('notes');
  };

  const activeNote = allNotes.find(n => n.topic_id === activeTopicId) || allNotes[0];
  const totalBookmarks = Object.values(bookmarks).filter(Boolean).length;

  return (
    <div className="h-screen w-screen bg-[#1c1c1f] text-[#d4d4d8] flex flex-col font-sans selection:bg-zinc-700 selection:text-white overflow-hidden">
      {/* Top Header Bar */}
      <TopNav
        viewMode={viewMode}
        setViewMode={setViewMode}
        fontSizeMultiplier={fontSizeMultiplier}
        setFontSizeMultiplier={setFontSizeMultiplier}
        totalBookmarksCount={totalBookmarks}
        onToggleSidebar={() => setSidebarOpen(prev => !prev)}
      />

      {/* Main Body Grid */}
      <div className="flex-1 flex overflow-hidden min-h-0">
        {/* Sidebar Index (Desktop: fixed column; Mobile: slide-over drawer) */}
        <Sidebar
          manifest={manifest}
          allNotes={allNotes}
          activeTopicId={activeTopicId}
          onSelectTopic={handleSelectTopic}
          completedTopics={completedTopics}
          onToggleComplete={handleToggleComplete}
          bookmarks={bookmarks}
          onToggleBookmark={handleToggleBookmark}
          isOpen={sidebarOpen}
          onClose={() => setSidebarOpen(false)}
          searchQuery={searchQuery}
          setSearchQuery={setSearchQuery}
          paperFilter={paperFilter}
          setPaperFilter={setPaperFilter}
        />

        {/* Dynamic Center Viewport */}
        <main className="flex-1 h-full overflow-y-auto bg-[#1c1c1f] min-w-0">
          {viewMode === 'notes' && (
            <TopicView
              note={activeNote}
              allNotes={allNotes}
              onSelectTopic={handleSelectTopic}
              isCompleted={!!completedTopics[activeNote?.topic_id]}
              onToggleComplete={handleToggleComplete}
              isBookmarked={!!bookmarks[activeNote?.topic_id]}
              onToggleBookmark={handleToggleBookmark}
              onOpenImage={(img) => setModalImage(img)}
              fontSizeMultiplier={fontSizeMultiplier}
            />
          )}

          {viewMode === 'mcqs' && (
            <McqPracticeView
              mcqBank={mcqBank}
              allNotes={allNotes}
              onSelectTopic={handleSelectTopic}
            />
          )}

          {viewMode === 'mains' && (
            <MainsBankView
              mainsBank={mainsBank}
              onSelectTopic={handleSelectTopic}
            />
          )}

          {viewMode === 'dashboard' && (
            <DashboardView
              manifest={manifest}
              allNotes={allNotes}
              completedTopics={completedTopics}
              bookmarks={bookmarks}
              onSelectTopic={handleSelectTopic}
              onSwitchMode={(mode) => setViewMode(mode)}
            />
          )}
        </main>
      </div>

      {/* Lightbox Image Zoom Modal */}
      {modalImage && (
        <ImageModal
          image={modalImage}
          onClose={() => setModalImage(null)}
        />
      )}
    </div>
  );
}
